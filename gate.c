#include <stdio.h>
#include <string.h>

void success() {
    printf("Success! The gate is open.\n");
}

int main(int argc, char** argv) {
   if (argc < 2 || argc > 2) {
        printf("Usage: ./gate [password]\n");
        return 0;
   }
   if (strcmp(argv[1], "hunter2") == 0) {
        success();
   } else {
        printf("ACCESS DENIED\n");
        return 1;
   }
   return 0;
}
