#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>

using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::vector;
using std::stoi;

typedef vector<vector<string> > VecOfVecOfStr;

VecOfVecOfStr read_file(string file_name, bool print_console = false) {
  string line;
  vector<vector<string> > v;
  ifstream myfile(file_name);
  if (myfile.is_open()) {
    while (getline(myfile, line)) {
      string buf;
      std::stringstream ss(line);
      vector<string> tokens;
      while (ss >> buf) tokens.push_back(buf);
      v.push_back(tokens);
    }
    myfile.close();
  } else
    cout << "Unable to open file" << endl;
  if (print_console) {
    for (const vector<string> &vec : v) {
      for (string x : vec) std::cout << x << ' ';
      std::cout << std::endl;

    }
  }
  return v;
}

long long int one_ring(long long int r) { return 1 + 2 * r; }

long long int how_many_rings(long long int r_start, long long int t) {
  long long int sum = 0;
  long long int i = 0;
  while (sum <= t) {
    sum += one_ring(r_start);
    r_start += 2;
    ++i;
  }
  return i - 1;
}

int main() {
  VecOfVecOfStr v = read_file("A-large-practice.in");
  int number_of_examples = stol(v[0][0]);
  // cout << "number of examples: " << number_of_examples << endl;
  for (int i = 1; i < number_of_examples + 1; ++i) {
    // cout << std::setw(20) << v[i][0]<< "\t" << std::setw(20) << v[i][1];
    // cout<<std::setw(10) << how_many_rings(stoll(v[i][0]), stoll(v[i][1])) <<
    // endl;
    cout << "Case #" << i << ": "
         << how_many_rings(stoll(v[i][0]), stoll(v[i][1])) << endl;
  }
  return 0;
}
