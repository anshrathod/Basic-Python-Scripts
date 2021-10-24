import java.util.*;
class Main {
  public static void main(String[] args) 
  {

    int x,p,tp=0,tc=0,n=4;
    String na;
    Scanner s = new Scanner(System.in);
    Random r = new Random();
    System.out.print("Enter name:");
    na = s.nextLine();
    while(n>0)
    {
      System.out.println("Enter \n 0.ROCK \n 1.PAPER \n 2.SCISSORS ");
      p = s.nextInt();
      x = r.nextInt(3);
      System.out.println("COMPUTER INPUT = "+ x);

      if((p == 0) && (x == 1))
      {
        tc++;
        System.out.println("computer  wins");
      }
      else if((p == 1) && (x == 0))
      {
        tp++;
        System.out.println(na  + "wins");
      }
      else if((p == 1) && (x == 2))
      {
        tc++;
        System.out.println( "computer  wins");
      }
      else if((p == 2) && (x == 1))
      {
        tp++;
        System.out.println(na  + "wins");
      }
      else if((p == 0) && (x == 2))
      {
        tp++;
        System.out.println(na  + "wins");
      }
      else if((p == 2) && (x == 0))
      {
        tc++;
        System.out.println( "computer  wins");
      } 
      else if(p == x)
      {
         System.out.println( "draw");
      }
      System.out.println("SCORE----------");
      System.out.println( "COMP:" +tc);
      System.out.println(na + ":" +tp);
      n--;
    }
   
   if(tp==tc)
   {
      System.out.println( "TIE");
   }
   else if(tp>tc)
   {
      System.out.println(na + " wins");
   }
   else 
   {
      System.out.println( "computer  wins");
   }

  }
}