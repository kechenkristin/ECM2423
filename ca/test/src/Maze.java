import java.util.Observable;
import java.util.Observer;
import java.util.TreeSet;

public class Maze {
    private Grid grid;
    private int width;
    private int length;

    private final String fileName;

    public Maze(String fn) {
        fileName = fn;
    }


    public void init() {
        grid = new Grid();
        grid.constructWidthLength(fileName);
        grid.constructGrid(fileName);
        width = grid.width;
        length = grid.length;
    }

    /**
     * Size of the maze, width * length
     */
    public int size() {
        return width * length;
    }

    /**
     * Total number of vertices in the maze
     */
    public int V() {
        return width * length;
    }

    /**
     * Returns the x coordinate of vertex v
     */
    public int toX(int v) {
        return v % width;
    }


    /**
     * Returns the y coordinate of vertex v
     */
    public int toY(int v) {
        return v / width;
    }

    public int xyTo1D(int x, int y) {
        return y * width + x;
    }

    /* Returns the neighbors of v */
    public Iterable<Integer> adj(int v) {
        int x = toX(v);
        int y = toY(v);

        TreeSet<Integer> neighbors = new TreeSet<>();

        if (inBounds(x - 1, y)) {
            if (grid.isPath(x - 1, y)) neighbors.add(xyTo1D(x - 1, y));
        }

        if (inBounds(x + 1, y)) {
            if (grid.isPath(x + 1, y)) neighbors.add(xyTo1D(x + 1, y));
        }

        if (inBounds(x, y - 1)) {
            if (grid.isPath(x, y - 1)) neighbors.add(xyTo1D(x, y - 1));
        }

        if (inBounds(x, y + 1)) {
            if (grid.isPath(x, y + 1)) neighbors.add(xyTo1D(x, y + 1));
        }
        return neighbors;
    }

    /**
     * Returns true if (x, y) is inside the bounds of the maze.
     */
    private boolean inBounds(int x, int y) {
        return (!(x == -1 || x == width || y == -1 || y == length));
    }


    public static void main(String[] args) {
        Maze m = new Maze("test.txt");
        System.out.println(m.toX(19));
        System.out.println(m.toY(19));
        System.out.println(m.xyTo1D(4, 3));
    }


}
