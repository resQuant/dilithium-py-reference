import dilithium
import argparse
import base64

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--security", type=int, choices=[2,3,5], default=2,
                    help="Select security level")
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="Print intermediate values")
    parser.add_argument("-k", "--keyfile", required=True, help="Files storing keys (pk with _pk, and sk with _sk")

    args = parser.parse_args()

    sec_lvl = args.security
    file_arg = args.keyfile
    sk_file_arg = file_arg+"_sk"
    pk_file_arg = file_arg+"_pk"



    if sec_lvl == 2:
        pk, sk = dilithium.Dilithium2.keygen()
    elif sec_lvl == 3:
        pk, sk = dilithium.Dilithium3.keygen()
    else:
        pk, sk = dilithium.Dilithium5.keygen()


    with open(sk_file_arg, "wb") as sk_file:
        sk_file.write(sk)
    

    with open(pk_file_arg, "wb") as pk_file:
        pk_file.write(pk)

    if args.verbose:
        print(base64.b64encode(sk))
        print(base64.b64encode(pk))

    
    