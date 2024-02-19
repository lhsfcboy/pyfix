import re

def parse_fix_log(fix_log):
    fix_dict = {}
    fix_fields = re.findall(r'(\d+)=(.*?)(?=\s+\d+=|$)', fix_log)

    for field in fix_fields:
        fix_dict[int(field[0])] = field[1]

    return fix_dict

if __name__ == "__main__":
    fix_log = "8=FIX.4.2  9=78  35=8  49=Sen 1 derCompID  56=TargetCompID  34=1  52=20240213-10:15:30  6=100.25  11=OrderID123  55=IBM  54=1  38=100  40=1 58=XXX YYY 10=003"

    fix_dict = parse_fix_log(fix_log)
    for key, value in fix_dict.items():
        print(f"{key}={value}")
