import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileOperation {
    public static int[] readFileLineByLine() throws IOException {
        BufferedReader reader;

        int[] ret = {0, 0};

        try {
            reader = new BufferedReader(new FileReader("res/maze/simpleMaze.txt"));


            String line = reader.readLine();

            /* count how many chars are in a string, remove space */
            int charCount = line.replace(" ", "").length();
            System.out.println(charCount);


            int lineCount = 0;

            while (line != null) {
                System.out.println(line);
                // read next line
                line = reader.readLine();
                lineCount++;
            }

            reader.close();
            System.out.println(lineCount);

            ret[0] = charCount;
            ret[1] = lineCount;
        } catch (IOException e) {
            e.printStackTrace();
        }

        return ret;
    }


    public static void constructGrid(int width, int length) {
        BufferedReader reader;


        try {
            reader = new BufferedReader(new FileReader("res/maze/simpleMaze.txt"));

            String line = reader.readLine();

            /* count how many chars are in a string, remove space */


            int lineNo = 0;
            boolean[][] grid = new boolean[length][width];

            while (line != null) {
                String cleanLine = line.replace(" ", "");
                System.out.println(cleanLine);

                for (int i = 0; i < width; i ++) {
                    grid[lineNo][i] = cleanLine.charAt(i) != '#';
                }

                // read next line
                line = reader.readLine();
                lineNo++;
            }

            reader.close();
            System.out.println(lineNo);

            for (int i = 0; i < length; i++) {
                for (int j = 0; j < width; j++) {
                    System.out.println(grid[i][j]);
                }
                System.out.println();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
        // FileOperation.readFileLineByLine();
        FileOperation.constructGrid(5, 4);
    }
}
