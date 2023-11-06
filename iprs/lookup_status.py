import argparse
from iprs_status_codes_list import status_codes

def get_status_info(status_codes_dict, status_code, flag):
    if status_code in status_codes_dict:
        if flag == "description":
            return f"{status_code} - {status_codes_dict[status_code]['description']}"
        elif flag == "comment":
            return f"{status_code} - {status_codes_dict[status_code]['comment']}"
        else:
            return "Invalid flag. Use --description or --comment."
    else:
        return "Status code not found."

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get description or comment for a status code")
    parser.add_argument("status_code", nargs="?", help="Status code to lookup")
    parser.add_argument("--description", action="store_const", const="description", dest="flag", help="Get description")
    parser.add_argument("--comment", action="store_const", const="comment", dest="flag", help="Get comment")

    args = parser.parse_args()
    status_code = args.status_code
    flag = args.flag

    if not status_code and not flag:
        print("Both comment and description for all status codes:")
        for code, data in status_codes.items():
            print(f"{code} - Description: {data['description']},\n \tComment: {data['comment']}\n")
    else:
        result = get_status_info(status_codes, status_code, flag)
        if result:
            print(result)
        else:
            print("Status code not found.")
