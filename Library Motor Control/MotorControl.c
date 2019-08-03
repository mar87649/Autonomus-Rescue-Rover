#include <msp430.h> 


int add(int a, int b){
    return (a+b);
}

void motor_A_clockwise(){
    // Rotate the Right Motor clockwise
    P2OUT |=  BIT0;        //enA    HIGH
    P2OUT |=  BIT1;        //in1    HIGH
    P2OUT &= ~BIT2;        //in2    LOW
}

void motor_A_counterclockwise(){
    // Rotate the Right Motor counter clockwise
    P2OUT |=  BIT0;        //enA    HIGH
    P2OUT &= ~BIT1;        //in1    LOW
    P2OUT |=  BIT2;        //in2    HIGH
}


void motor_B_clockwise(){
    // Rotate the Left Motor clockwise
    P2OUT |=  BIT5;        //enB    HIGH
    P2OUT |=  BIT3;        //in3    HIGH
    P2OUT &= ~BIT4;        //in4    LOW
}

void motor_B_counterclockwise(){
    // Rotate the Left Motor clockwise
    P2OUT |=  BIT5;        //enB    HIGH
    P2OUT &= ~BIT3;        //in3    LOW
    P2OUT |=  BIT4;        //in4    HIGH
}

void move_forward(){
    motor_A_clockwise();
    motor_B_clockwise();
}

void move_reverse(){
    motor_A_counterclockwise();
    motor_B_counterclockwise();
}

void turn_left(){
    motor_A_counterclockwise();
    motor_B_clockwise();
}

void turn_right(){
    motor_A_clockwise();
    motor_B_counterclockwise();
}

void stop(){
    P2OUT &= ~BIT0;        //enA    LOW
    P2OUT &= ~BIT5;        //enB    LOW
}
//========================================================================================
//    P2OUT |=  BIT1;              // P2.1 = 1,
//    P2OUT &= ~BIT2;              // P2.2 = 0

//    P1OUT |= (BIT3 + BIT4 );        //turn enA enB      high
//    P2OUT |= (BIT0 + BIT1);         //turn in2 in3      high
//
//    P1OUT &= ~(BIT3 + BIT4 + BIT5 );//turn enA enB in1  low
//    P2OUT &= ~(BIT1);               //turn in3          low
