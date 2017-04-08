#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <map>

using std::cout;
using std::vector;
using std::map;
using std::string;
using std::ifstream;
using std::endl;
using std::pair;
using std::reverse;
using std::to_string;
using std::stol;
using std::stringstream;

typedef vector<vector<int> > VecOfVecOfInts;

struct example {
  int B;          // number of barbers
  int M[100000];  // time of each barber
  int N;          // number in the line
};

VecOfVecOfInts read_file(string file_name, bool print_console = false) {
  string line;
  VecOfVecOfInts v;
  ifstream myfile(file_name);
  if (myfile.is_open()) {
    while (getline(myfile, line)) {
      string buf;
      stringstream ss(line);
      vector<int> tokens;
      while (ss >> buf) tokens.push_back(stoi(buf));
      v.push_back(tokens);
    }
    myfile.close();
  } else
    cout << "Unable to open file" << endl;
  if (print_console) {
    for (const vector<int> &vec : v) {
      for (int x : vec) cout << x << ' ';
      cout << endl;
    }
  }
  return v;
}

example read_example(VecOfVecOfInts v, int case_number) {
  example test;
  test.B = v[1 + case_number * 2][0];
  test.N = v[1 + case_number * 2][1];
  for (int i = 0; i < test.B; ++i) {
    test.M[i] = v[2 + case_number * 2][i];
  }
  return test;
}

int perform_haircut(example test) {
  std::vector<int> time_i(test.B);
  // std::fill_n(time_i, test.B, 0);
  for (int i = 0; i < test.N - 1; ++i) {
    std::vector<int>::iterator min =
        std::min_element(std::begin(time_i), std::end(time_i));
    int index_of_min = std::distance(std::begin(time_i), min);
    time_i[index_of_min] += test.M[index_of_min];
    // cout << time_i[0]<< " " << time_i[1]<<endl;
  }
  std::vector<int>::iterator min =
      std::min_element(std::begin(time_i), std::end(time_i));
  int index_of_min = std::distance(std::begin(time_i), min);
  return index_of_min + 1;
}

int main() {
  VecOfVecOfInts v = read_file("workfile.in");
  int number_of_examples = v[0][0];
  // cout << "number of examples: " << number_of_examples << endl;
  for (int i = 0; i < number_of_examples; ++i) {
    example test = read_example(v, i);
    cout << "Case #" << i + 1 << ": " << perform_haircut(test) << endl;
  }

  return 0;
}
