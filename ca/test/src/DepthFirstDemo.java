
/**
 *  @author Josh Hug
 */
public class DepthFirstDemo {
    /* Runs a depth first search from (1, 1) to (N, N) on the graph in the config file. */

    public static void main(String[] args) {
        Maze maze = new Maze("simpleMaze.txt");
        maze.init();

        int startX = 1;
        int startY = 0;
        int targetX = 2;
        int targetY = 3;

        MazeExplorer mdfp = new MazeDepthFirstPaths(maze, startX, startY, targetX, targetY);
        mdfp.solve();
    }

}
