import dilithium
import argparse
import base64

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--security", type=int, choices=[2,3,5], default=2,
                    help="Select security level")
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="Print intermediate values")
    parser.add_argument("-k", "--keyfile", required=True, help="File storing private key")
    parser.add_argument("-sig", "--signature", required=True, help="File for signature")
    parser.add_argument("-m", "--message", required=True, help="Message file")

    args = parser.parse_args()

    sec_lvl = args.security
    file_arg = args.keyfile
    msg_file_arg = args.message
    signature_file_arg = args.signature
    sk_file_arg = file_arg

    f = open(sk_file_arg, mode="rb")
    sk = f.read()
    f.close()
    f = open(msg_file_arg, mode="rb")
    m = f.read()
    f.close()
    
    if sec_lvl == 2:
        sig = dilithium.Dilithium2.sign(sk,m)
    elif sec_lvl == 3:
        sig = dilithium.Dilithium3.sign(sk,m)
    else:
        sig = dilithium.Dilithium5.sign(sk,m)

    with open(signature_file_arg, "wb") as signature_file:
        signature_file.write(sig)
    

    if args.verbose:
        print(base64.b64encode(sig))
