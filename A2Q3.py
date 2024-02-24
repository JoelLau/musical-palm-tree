from libs.tabu_bigrams import count_tabu_free, parse_raw

def main():
    """
    continuously takes in raw input and prints the number of tabu 
    free bigrams
    
    expected raw input: [m n ...excluded_bigrams]
    """
    while(True):
        try:
            raw = input()
            result = count_tabu_free(raw)

            print(result)

        except ValueError:
            # exit program
            print("ValueError - exiting program")
            break;


if __name__ == "__main__":
    main()
