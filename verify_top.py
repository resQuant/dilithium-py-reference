import dilithium
import argparse
import base64

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--security", type=int, choices=[2,3,5], default=2,
                    help="Select security level")
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="Print intermediate values")
    parser.add_argument("-k", "--keyfile", required=True, help="Public key file")
    parser.add_argument("-sig", "--signature", required=True, help="Signature file")
    parser.add_argument("-m", "--message", required=True, help="Message file")

    args = parser.parse_args()

    sec_lvl = args.security
    file_arg = args.keyfile
    msg_file_arg = args.message
    signature_file_arg = args.signature
    pk_file_arg = file_arg

    f = open(pk_file_arg, mode="rb")
    pk = f.read()

    f.close()
    f = open(signature_file_arg, mode="rb")
    sig = f.read()

    f.close()
    f = open(msg_file_arg, mode="rb")
    m = f.read()
    f.close()

    dilithium.Dilithium2.verify(pk,m,sig)
    if sec_lvl == 2:
        res = dilithium.Dilithium2.verify(pk,m,sig)
    elif sec_lvl == 3:
        res = dilithium.Dilithium3.verify(pk,m,sig)
    else:
        res = dilithium.Dilithium5.verify(pk,m,sig)

    print(res)
    


