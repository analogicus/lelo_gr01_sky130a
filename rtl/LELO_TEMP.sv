


module LELO_TEMP(input clk, input rst, input request, input oscillator_clk, output pwr, output done, output logic[7:0] out);


    reg [7:0] counter;
    logic reset_counter;


   
    enum {IDLE, MEASURE, STORE, PULSE} current_state, next_state;



    //Switching to the next state
    always_ff @ (posedge clk, posedge rst) 
    begin
        if (rst)  current_state <= IDLE;
        else      current_state <= next_state;
    end;



    //Computing the next state
    always_comb 
    begin
        case(current_state)
            IDLE: 
                if (request) next_state = MEASURE;
                else         next_state = IDLE;
            
            MEASURE:         next_state = STORE;

            STORE:           next_state = PULSE;
            PULSE:           next_state = IDLE;
        endcase
    end;



    //Counting the pulses from the oscillator
    always_ff @(posedge oscillator_clk or posedge reset_counter or posedge rst)
    begin
        if (reset_counter || rst)          counter <= 0;
        else if (current_state==MEASURE)   counter <= counter + 1;
    end



    //Updating the out value with the counter
    always_ff @(posedge clk or posedge rst)
    begin
        if (rst)                out <= 0;
        else if (current_state==STORE)  out <= counter;
    end



    //Updating the intern and extern signals
    assign           pwr = (current_state == MEASURE);
    assign          done = (current_state == PULSE);
    assign reset_counter = (current_state == IDLE);



endmodule
