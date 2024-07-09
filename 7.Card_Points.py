def maxScore(cardpoints, k):
    n = len(cardpoints)
    
    
    current_sum = sum(cardpoints[:k])
    max_sum = current_sum
    
    
    for i in range(k):
        current_sum += cardpoints[n - 1 - i] - cardpoints[k-1-i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def main():
    
    cardpoints = list(map(int, input("Enter the card points:").split()))
    k = int(input("Enter number of cards:"))
    
    
    print("Max score:", maxScore(cardpoints, k))

if __name__ == "__main__":
    main()
