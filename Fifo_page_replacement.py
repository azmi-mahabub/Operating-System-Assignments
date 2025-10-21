def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    print("Page Reference String:", pages)
    print(f"Number of Frames: {capacity}\n")

    for i, page in enumerate(pages):
        print(f"Step {i+1}: Referencing page {page}")

        if page not in memory:

            if len(memory) < capacity:
                memory.append(page)
            else:
                removed_page = memory.pop(0)
                memory.append(page)
                print(f"  Page {removed_page} replaced by {page}")

            page_faults += 1
            print(f"  Page Fault! Memory: {memory}")
        else:
            print(f"  Page Hit! Memory: {memory}")

        print()
    print(f"Total Page Faults: {page_faults}")
    print(f"Total Page Hits: {len(pages) - page_faults}")
    print(f"Page Fault Ratio: {page_faults}/{len(pages)}")

    return page_faults


if __name__ == "__main__":
    page_reference_string = [3, 2, 0, 1, 0, 5, 9, 1, 2]
    frame_capacity = 3

    page_faults = fifo_page_replacement(page_reference_string, frame_capacity)