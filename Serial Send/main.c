#include <msp430.h> 

const char string[] = { "Hello World\r\n" };

void Initial_Setup()
{
    WDTCTL = WDTPW + WDTHOLD;                                              // Stop watch dog timer
    DCOCTL = 0;                                                            // reset clock to zero
    BCSCTL1 = CALBC1_1MHZ;
    DCOCTL = CALDCO_1MHZ;                                                  // submainclock 1mhz

    P1IFG  = 0x00;                                                         //clear all interrupt flags
    TA0CCR0 = 20000-1;                                                     // PWM Period TA0.1
    TA0CCR1 = 1500;                                                        // CCR1 PWM duty cycle
    TA0CCTL1 = OUTMOD_7;                                                   // CCR1 reset/set
    TA0CTL   = TASSEL_2 + MC_1;                                            // SMCLK, up mode

    P2DIR |= 0xFF; // All P2.x outputs
    P2OUT &= 0x00; // All P2.x reset
    P1SEL |= RXD + TXD ; // P1.1 = RXD, P1.2=TXD
    P1SEL2 |= RXD + TXD ; // P1.1 = RXD, P1.2=TXD
    P1DIR |= RXLED + TXLED;
    P1OUT &= 0x00;
    UCA0CTL1 |= UCSSEL_2; // SMCLK
    UCA0BR0 = 0x08; // 1MHz 115200
    UCA0BR1 = 0x00; // 1MHz 115200
    UCA0MCTL = UCBRS2 + UCBRS0; // Modulation UCBRSx = 5
    UCA0CTL1 &= ~UCSWRST; // **Initialize USCI state machine**
    UC0IE |= UCA0RXIE; // Enable USCI_A0 RX interrupt
    __bis_SR_register(CPUOFF + GIE); // Enter LPM0 w/ int until Byte RXed


    return;
}

int main(void){
    setup();
    UCA0TXBUF = string[i++]
}
