import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;

public class random {

    public static void main(String[] args) {
        int[] sizes = {10, 100, 1000, 10_000, 100_000, 1_000_000, 10_000_000};
        int runs = 10;
        int range = 1_000_000;

        try (FileWriter csvWriter = new FileWriter("benchmark_results.csv")) {
            csvWriter.write("ArraySize,AverageTimeMillis\n");

            for (int size : sizes) {
                long totalTime = 0;

                for (int i = 0; i < runs; i++) {
                    int[] array = generateRandomArray(size, range);

                    long startTime = System.nanoTime();
                    int max = findMax(array);
                    long endTime = System.nanoTime();

                    long duration = (endTime - startTime) / 1_000_000; // Convert to milliseconds
                    totalTime += duration;
                }

                double averageTime = totalTime / (double) runs;
                System.out.println("Size: " + size + " -> Avg Time: " + averageTime + " ms");

                csvWriter.write(size + "," + averageTime + "\n");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static int[] generateRandomArray(int size, int bound) {
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(bound);
        }
        return array;
    }

    public static int findMax(int[] array) {
        int max = Integer.MIN_VALUE;
        for (int value : array) {
            if (value > max) {
                max = value;
            }
        }
        return max;
    }
}
