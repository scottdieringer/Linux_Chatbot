#!/usr/bin/env python3

# Tree structure representing the troubleshooting decision tree.
class Node:
    def __init__(self, question=None, answer=None):
        self.question = question  # Question to ask
        self.answer = answer  # Advice or final message if leaf
        self.children = {}  # Map of responses ("y"/"n") to child Nodes

# Recursive transversal through decision tree.
def traverse(node):
    if node.answer:
        # Leaf node: print advice
        print("\n" + node.answer + "\n")
        return

    # Ask question
    while True:
        response = input(node.question + " (Y/N): ").strip().lower()
        if response in node.children:
            traverse(node.children[response])
            break
        else:
            print("⚠️ Please answer Y or N.\n")


def build_performance_tree():
    # Leaf nodes
    cpu_issue = Node(answer="✅ That’s probably the issue!\n"
                            "👉 Run `top` or `htop` to find the process ID (PID).\n"
                            "👉 Then stop it with: kill -9 <PID>\n")

    disk_issue = Node(answer="✅ That explains the slowdown.\n"
                             "👉 You can clean logs or find big files with:\n"
                             "   du -sh /* | sort -h\n")

    memory_issue = Node(answer="👉 Finally let’s check memory usage. Run `free -h`.\n"
                               "If swap usage is high, your system may be running out of RAM.\n"
                               "Closing programs or adding swap space could help.\n")

    # Intermediate nodes
    check_disk = Node(question="👉 Okay, let’s check disk space. Run `df -h`. Is your disk almost full?\n")
    check_disk.children = {"y": disk_issue, "n": memory_issue}

    # Updated CPU node with guidance first
    cpu_guidance = Node(
        answer="👉 First, run `top` to see a list of processes and the percentage CPU that each is using.\n"
               "Then answer the next question.\n")

    check_cpu = Node(question="Do you see one process using a lot of CPU or memory, maybe more than 90%?\n", answer=None)
    # Attach children
    check_cpu.children = {"y": cpu_issue, "n": check_disk}

    # Combine guidance + question
    cpu_guidance.children = {"continue": check_cpu}  # We'll use 'continue' as a dummy trigger to move to the question

    return cpu_guidance


def main():
    print("👋 Hi, I’m your Linux Troubleshooting Bot!\n")
    print("You said your system feels slow. Let’s figure out why.\n")

    tree = build_performance_tree()
    print(tree.answer)
    traverse(tree.children["continue"])

    print("🎉 Done! Thanks for troubleshooting with me.\n")


if __name__ == "__main__":
    main()
