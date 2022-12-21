import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class solve {
    final static long key = 811589153;

    static class Node {
        Node prev;
        Node next;
        long val;

        Node(Node prev, Node next, long val) {
            this.prev = prev;
            this.next = next;
            this.val = val;
        }
    }

    public static void main(String[] args) throws IOException {
        part1();
        part2();
    }

    public static void part1() throws IOException {
        List<Node> nodeList = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        Node head = null;
        Node prev = null;
        while (reader.ready()) {
            int num = Integer.parseInt(reader.readLine().strip());
            Node node = new Node(prev, null, num);
            nodeList.add(node);
            if (head == null) {
                head = node;
            }
            if (prev != null) {
                prev.next = node;
            }
            prev = node;
        }

        head.prev = prev;
        prev.next = head; // make the linked list circular

        for (Node node : nodeList) {
            head = swap(head, node, node.val % (nodeList.size() - 1));
        }

        Node cur = head;
        Node zero = null;
        for (int i = 0; i < nodeList.size(); i++) {
            if (cur.val == 0) {
                zero = cur;
            }
            cur = cur.next;
        }
        int sum = 0;
        for (int i = 1; i <= 3000; i++) {
            zero = zero.next;
            if (i % 1000 == 0) {
                System.out.println(zero.val);
                sum += zero.val;
            }
        }
        System.out.println(sum);

        reader.close();
    }

    public static void part2() throws IOException {
        List<Node> nodeList = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        Node head = null;
        Node prev = null;
        while (reader.ready()) {
            long num = Integer.parseInt(reader.readLine().strip()) * key;
            Node node = new Node(prev, null, num);
            nodeList.add(node);
            if (head == null) {
                head = node;
            }
            if (prev != null) {
                prev.next = node;
            }
            prev = node;
        }

        head.prev = prev;
        prev.next = head; // make the linked list circular

        for (int i = 0; i < 10; i++) {
            for (Node node : nodeList) {
                head = swap(head, node, node.val % (nodeList.size() - 1));
            }
        }

        Node cur = head;
        Node zero = null;
        for (int i = 0; i < nodeList.size(); i++) {
            if (cur.val == 0) {
                zero = cur;
            }
            cur = cur.next;
        }
        long sum = 0;
        for (int i = 1; i <= 3000; i++) {
            zero = zero.next;
            if (i % 1000 == 0) {
                System.out.println(zero.val);
                sum += zero.val;
            }
        }
        System.out.println(sum);

        reader.close();
    }

    public static Node swap(Node head, Node node, long time) {
        if (time == 0) {
            return head;
        }
        if (time > 0) {
            node = node.next;
        }
        if (head == node) {
            head = node.prev;
        } else if (head == node.prev) {
            head = node;
        }
        node.next.prev = node.prev;
        node.prev.next = node.next;
        node.next = node.prev;
        node.prev = node.next.prev;
        node.next.prev = node;
        node.prev.next = node;
        if (time > 0) {
            node = node.next;
        }
        return swap(head, node, time > 0 ? time - 1 : time + 1);
    }
}