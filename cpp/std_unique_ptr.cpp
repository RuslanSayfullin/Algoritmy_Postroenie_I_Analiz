#include <iostream>
#include <memory>

int maint() {
    // создание умного указателя, который владеет динамический выделенным целым числом.
    std::unique_ptr<int> myUniquePtr = std::make_unique<int>(42);

    // использование умного указателя как обычного указателя.
    int value = *myUniquePtr;

    return 0;
}