#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <list>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::list;

void read_file() {
  string line;
  ifstream myfile("example.in");
  std::list<int> lines;
  if (myfile.is_open()) {
    while (getline(myfile, line)) {
      cout << (typeid(line) == typeid(std::string)) << '\n';
    }
    myfile.close();
  } else
    cout << "Unable to open file";
}

int main() {
  int t, n, m;
  t = 0;
  read_file();
  for (int i = 1; i <= t; ++i) {
    cin >> n >> m;  // read n and then m.
    cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
  }
}
