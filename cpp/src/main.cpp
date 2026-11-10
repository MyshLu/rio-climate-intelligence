#include <iostream>
#include <string_view>

int main()
{
    constexpr std::string_view project_name =
        "Rio Climate Intelligence";

    constexpr int cxx_standard = 20;

    std::cout << "Project: " << project_name << '\n';
    std::cout << "C++ standard: " << cxx_standard << '\n';
    std::cout << "Development environment ready!\n";

    return 0;
}
