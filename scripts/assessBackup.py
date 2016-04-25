import hashlib
import os
import argparse



def grabS3(s3url, rootdir):
    """Grab S3 stored backup if not present in s3 directory (root dir)."""
    print('checking for s3 copy locally.')
    if not os.listdir(rootdir):
        print('no s3 backup copy locally. Syncing now.')
        if not s3url.startswith('s3:') or rootdir.startswith('s3:'):
            print('check your arguments for s3 sync or run manually.')
        else:
            s3cmd = 's3cmd sync ' + s3url + ' ' + rootdir
        os.system(s3cmd)
    else:
        print('have s3 copy locally.')


def convertXMLtoDict():



def main():
    """Assess the S3 Bepress backup instance data."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", dest="rootdir",
                        help="root directory of backup")
    parser.add_argument("-s", "--s3", dest="s3url",
                        help="s3 (backup location) url")

    args = parser.parse_args()

    if not len(sys.argv) > 0:
        parser.print_help()
        parser.exit()

    grabS3(args.s3url, args.rootdir)




if __name__ == "__main__":
    main()
