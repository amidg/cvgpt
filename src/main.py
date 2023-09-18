import os
import argparse
from gusevtech.cvgpt.builder import Resume, Portfolio

# main program
def main():
    # parse args before doing anything else
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", help="let the software work on your resume")
    parser.add_argument("--portfolio", help="work your portfolio database")
    args = parser.parse_args()

    # if we work on the resume
    if args.resume:
        print("work in progress")
    # if we work on the portfolio database
    if args.portfolio:
        portfolio = Portfolio()

if __name__ == "__main__":
    main()
