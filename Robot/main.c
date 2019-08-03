//Input Output Diagram/////////////////////////////////////////////////////
//                  -------
//      (VCC)    --|       |--   (Ground)
//      (P1.0)   --|       |--   (XIN)
//RX Pin(P1.1)   --|       |--   (XOUT)
//TX Pin(P1.2)   --|       |--   (TEST)
//      (P1.3)   --|       |--   (RST)
//      (P1.4)   --|       |--   (P1.7)
//      (P1.5)   --|       |--   (P1.6)
//ENA   (P2.0)   --|       |--   (P2.5) ENB
//IN1   (P2.1)   --|       |--   (P2.4) IN3
//IN2   (P2.2)   --|       |--   (P2.3) IN4
//                  -------
//Includes/////////////////////////////////////////////////////////////////
#include <msp430g2553.h>
#include <stdio.h>
#include <MotorControl.h>
#define TXLED BIT0
#define RXLED BIT6
#define TXD BIT2
#define RXD BIT1
//#include <BTCommunication>
//Global Variables//////////////////////////////////////////////////////////
int BTCom = 0;
int mov = 0;
const char string[] = { "Hello World\r\n" };
unsigned int i; //Counter
//Function Declarations/////////////////////////////////////////////////////
void Initial_Setup();
void General_Pin_Setup();
//Initial Setup Function//////////////////////////////////////////////////
void Initial_Setup()
{
    WDTCTL = WDTPW + WDTHOLD;                                              // Stop watch dog timer
    DCOCTL = 0;                                                          // reset clock to zero
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
//Pin Setup FUnction//////////////////////////////////////////////////////
void General_Pin_Setup()
{
    P2DIR |=  (BIT0 + BIT1 + BIT2 + BIT3 + BIT4 + BIT5);
    P2OUT &= ~(BIT0 + BIT1 + BIT2 + BIT3 + BIT4 + BIT5);                                                        // P1.6 select TA0.1 option
    return;
}
//Main Loop////////////////////////////////////////////////////////////////
int main(void)
{
   Initial_Setup();
   General_Pin_Setup();
      while (1){

      }
}
///////////////////////////////////////////////////////////////////////////////
#pragma vector=USCIAB0TX_VECTOR
__interrupt void USCI0TX_ISR(void)
{
   P1OUT |= TXLED;
     UCA0TXBUF = string[i++]; // TX next character
    if (i == sizeof string - 1) // TX over?
       UC0IE &= ~UCA0TXIE; // Disable USCI_A0 TX interrupt
    P1OUT &= ~TXLED; }

#pragma vector=USCIAB0RX_VECTOR
__interrupt void USCI0RX_ISR(void)
{
   P1OUT |= RXLED;
          switch(UCA0RXBUF) {
              case 'w' : move_forward(); i = 0; UC0IE |= UCA0TXIE; UCA0TXBUF = string[i++];break;
              case 's' : move_reverse(); i = 0; UC0IE |= UCA0TXIE; UCA0TXBUF = string[i++];break;
              case 'a' : turn_left();    i = 0; UC0IE |= UCA0TXIE; UCA0TXBUF = string[i++];break;
              case 'd' : turn_right();   i = 0; UC0IE |= UCA0TXIE; UCA0TXBUF = string[i++];break;
              default  : stop();         i = 0; UC0IE |= UCA0TXIE; UCA0TXBUF = string[i++];break;
          }
//    if (UCA0RXBUF == 'w') // 'a' received?
//    {
//       i = 0;
//       UC0IE |= UCA0TXIE; // Enable USCI_A0 TX interrupt
//      UCA0TXBUF = string[i++];
//    }
    P1OUT &= ~RXLED;
}
