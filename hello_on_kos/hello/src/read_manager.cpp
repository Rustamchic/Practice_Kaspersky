#include "read_manager.h"

#include <iostream>
#include <fstream>
#include <string>

bool ReadManager::Read(const std::string& helloListFileName)
{
    std::ifstream helloListFile;

    helloListFile.open(helloListFileName);
    if (!helloListFile.is_open())
    {
        return false;
    }

    for (std::string word; helloListFile >> word;)
    {
        m_wordList.push_back(word);
    }

    helloListFile.close();

    return m_wordList.size() > 0;
}