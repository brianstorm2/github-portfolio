import java.util.Scanner;
import java.sql.*;

public class Main {
    public static void main(String[] args) throws SQLException {
        String jdbcUrl = "jdbc:postgresql://localhost:5432/matts_login_page";
        String dbUser = "postgres";
        String dbPass = "admin";

        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcUrl, dbUser, dbPass); //connection attempt on db
        } catch (SQLException e) {
            throw new RuntimeException(e); //exception if connection fails
        }
        if (connection != null) {
            System.out.println("Welcome to Matt's Login Program!");
        }

        Scanner optionMenu = new Scanner(System.in); //scanner for user input
        Scanner userName = new Scanner(System.in);
        Scanner passWord = new Scanner(System.in);

        System.out.print("""
                1. Create a new account
                2. Login to account
                Enter Menu Option:""");

        int option = optionMenu.nextInt(); //parsing option choice

        if (option == 1) {
            System.out.print("Enter new username: ");
            String username = userName.nextLine(); //parsing username
            System.out.print("Enter new password: ");
            String password = passWord.nextLine(); //parsing password

            int passwordHashed = password.hashCode(); //generates a hash of the password so the password is not stored on the db
            String passwordHash = String.valueOf(passwordHashed); //converted to a string to be stored on the db

            String insertDetails = "INSERT INTO users(username, password) VALUES (?, ?)"; //insert command SQL
            PreparedStatement preparedStatement = connection.prepareStatement(insertDetails);
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, passwordHash);

            int rowsAffected = preparedStatement.executeUpdate(); //uploads user input to db

            System.out.println("Thanks for creating your account, " + username + "!");
            System.out.println("Your account details have been added to the database");

        }
        else if (option == 2) {
            String userExists = "f";  //set userExists and correctPassword to false to initialise while loop
            String correctPassword = "f";
            int passwordAttempts = 0; //attempt counter to prevent bruteforcing

            while (userExists.equals("f")) {
                System.out.print("Enter username: ");
                String username = userName.nextLine();

                String verifyUsername = "SELECT CASE WHEN EXISTS (SELECT 1 FROM users WHERE username = ?) THEN true ELSE false END AS user_exists"; //SQL command to check user exists
                PreparedStatement usernameStatement = connection.prepareStatement(verifyUsername);
                usernameStatement.setString(1, username);
                ResultSet resultSet = usernameStatement.executeQuery();
                resultSet.next();
                userExists = resultSet.getString("user_exists");
                if (userExists.equals("t")) {
                    while (correctPassword.equals("f")) {
                        System.out.print("Enter password: ");
                        String password = passWord.nextLine();

                        int passwordHashed = password.hashCode();
                        String passwordHash = String.valueOf(passwordHashed);
                        String verifyPassword = "SELECT CASE WHEN EXISTS (SELECT 1 FROM users WHERE password = ?) THEN true ELSE false END AS correct_password"; //SQL command to check password hash is correct
                        PreparedStatement passwordStatement = connection.prepareStatement(verifyPassword);
                        passwordStatement.setString(1, passwordHash);
                        resultSet = passwordStatement.executeQuery();
                        resultSet.next(); //set resultset cursor onto first row
                        correctPassword = resultSet.getString("correct_password");
                        if (correctPassword.equals("t")) {
                            System.out.println("Welcome" + username + "!");
                            break;
                        }
                        else if (passwordAttempts >= 3) {
                            System.out.println("Access denied for security purposes. Try again later"); //attempts failsafe
                            break;
                        }
                        else {
                            System.out.println("Wrong password, try again");
                            passwordAttempts++; //attempts += 1
                            }
                        }
                    }
                else {
                    System.out.println("Wrong username, try again");
                }
            }
        }

    }
}
