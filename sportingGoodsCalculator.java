import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Scanner;

public class sportingGoodsCalculator {
    public static void main(String[] args) {

        Dictionary<String, Integer> sportingGoods = new Hashtable<>(); //Create dictionary for sporting goods
        sportingGoods.put("tennis racket", 50); //name = key, price = value
        sportingGoods.put("football", 15);
        sportingGoods.put("basketball", 20);
        sportingGoods.put("boxing gloves", 35);

        Scanner sportItem = new Scanner(System.in); //scanner for user input
        Scanner quantity = new Scanner(System.in);
        Scanner moreGoods = new Scanner(System.in);

        String moreInput = "Y";
        int total = 0;

        while (moreInput.equalsIgnoreCase("Y")) { //while continue = y

            int subTotal = 0;

            System.out.println("Enter sporting good");
            String itemInput = sportItem.nextLine();

            System.out.println("Enter quantity:");
            int quantityInput = Integer.parseInt(quantity.nextLine());

            subTotal = sportingGoods.get(itemInput) * quantityInput; //dictionary look-up
            total += subTotal;
            System.out.println("Current total £" + total);

            System.out.println("Continue? Y/N");
            moreInput = moreGoods.nextLine();
        }
        System.out.println("Thank you for using the program!");
        System.out.println("Final Total £" + total);
    }
}
