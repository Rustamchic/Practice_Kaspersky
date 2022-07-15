#include "read_manager.h"
#include "file_names.h"

#include <iostream>
#include <fstream>
#include <time.h>

const std::string Tag = "[ReadManager] ";
const std::string ErrorTag = "[Error] ";

void HelloListOutput(const WordList& words)
{
    for(const auto& Word : words)
    {
        std::cout << Word << std::endl;
    }
}

void OpenUnavailableFile(const std::string &fileName)
{
    std::cout << Tag << "Try to read unavailable file '" << fileName << "'" << std::endl;

    std::ifstream inpFile;
    inpFile.open(fileName);
    if (!inpFile.is_open())
    {
        std::cout << Tag << "Unable to open the '" << fileName << "' file. It is correct behaviour." << std::endl;
    }
    else
    {
        std::cout << Tag << ErrorTag << "The '" << fileName << "' file is open. It is not correct behaviour." << std::endl;
    }
}

int main(int argc, char* argv[])
{
    try
    {
        ReadManager file;

        // Read the file we have access to.
        std::cout << Tag << "Try to read '" << HelloListFileName << "' file" << std::endl;
        if (!file.Read(HelloListFileName))
        {
               std::cout << Tag << ErrorTag << "Unable to read file: '" << HelloListFileName << "'" << std::endl;
        }
        else
        {
            std::cout << Tag << "Success" << std::endl;
            HelloListOutput(file.Get());
        }
    }
    catch(std::exception& ex)
    {
        std::cout << Tag << ErrorTag << ex.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}