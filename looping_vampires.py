#!/user/bin/env python3
def main():
    ## file line counter
    vamp_count = 0

    ## open the dracula text in read mode
    with open("dracula.txt", "r") as dracula_text:
        ## write to a new file
        with open("vampytimex.txt", "w") as fang:
            ## if the line contains vampire, display it, increment the counter, and write to the 2nd file
            for line in dracula_text:
                if 'vampire'  in line.lower():
                    print(line)
                    vamp_count += 1
                    fang.write(line)

    ## display counter when done
    print(f"Vampire appeared in {vamp_count} lines.")
if __name__ == '__main__':
    main()
