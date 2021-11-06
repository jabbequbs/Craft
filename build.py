#! python3

import glob
import os
import subprocess

def main():
    source_files = glob.glob(os.path.join("src", "*.c"))
    source_files += list(map(os.path.normpath, (
        "deps/lodepng/lodepng.c",
        "deps/glad/glad_gl.c",
        "deps/noise/noise.c",
        "deps/tinycthread/tinycthread.c",
        )))
    includes = list(map(os.path.normpath, (
        "deps/lodepng",
        "deps/noise",
        "deps/glad",
        "deps/tinycthread",
        )))
    libs = [
        "-lglfw3",
        "-lsqlite3",
        "-llibcurl",
        "-lWs2_32",
        "-lm",
        ]

    command = ["tcc"] + source_files
    for include in includes:
        command += ["-I"+include]
    command.extend(libs)
    command.extend(("-D", "__MINGW32__", "-o", "Craft.exe"))

    print(command)
    subprocess.call(command)

if __name__ == '__main__':
    main()
