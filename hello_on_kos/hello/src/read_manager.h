/* © 2021 AO Kaspersky Lab */
#ifndef HELLO_ON_KOS_READ_MANAGER_H
#define HELLO_ON_KOS_READ_MANAGER_H

#include <list>
#include <string>

typedef std::list<std::string> WordList;

class ReadManager
{
public:
// @brief Reads line from the user list file and stores in m_userList.
// This function is used only to demonstrate the ability to read from a file
// and does not carry another payload.
// @param[in] path specification of the file we want to read
// @return true if successful, otherwise false
    bool Read(const std::string& path);

// @brief Gets the contents of the m_userList variable.
// @return constant reference to m_userList
    const WordList &Get()
    {
        return m_wordList;
    }

private:
    WordList m_wordList;
};

#endif