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


typedef vector<vector<string> > VecOfVecOfStr;

VecOfVecOfStr read_file(string file_name, bool print_console = false) {
  string line;
  vector<vector<string> > v;
  ifstream myfile(file_name);
  if (myfile.is_open()) {
    while (getline(myfile, line)) {
      string buf;
      stringstream ss(line);
      vector<string> tokens;
      while (ss >> buf) tokens.push_back(buf);
      v.push_back(tokens);
    }
    myfile.close();
  } else
    cout << "Unable to open file" << endl;
  if (print_console) {
    for (const vector<string> &vec : v) {
      for (string x : vec) cout << x << ' ';
      cout << endl;
    }
  }
  return v;
}

bool compare(pair<long, int> i, pair<long, int> j) {
  return i.second < j.second;
}

long reverse(long last_number) {
  string str = to_string(last_number);
  reverse(str.begin(), str.end());
  last_number = stol(str);
  return last_number;
}

long count(long boundary) {
  long counter = 0;
  while (boundary > 0) {
    // cout<<"i:"<<boundary<<endl;
    map<int, long> my_map;
    my_map[1] = boundary;
    for (int i = 2; i < 11; ++i) {
      if (reverse(boundary - i) % 10 != 0 && boundary > 0 && reverse(boundary - i) > 0) {
        my_map[i - 1] = reverse(boundary - i - 1);
        cout << i - 1 << ":" << reverse(boundary - i - 1) << endl;
      }
    }
    pair<long, long> min =
        *min_element(my_map.begin(), my_map.end(), compare);

    counter += min.first;
    boundary -= min.second;

    // if (reverse(boundary) < boundary && boundary % 10 != 0) {
    // boundary = reverse(boundary);
    // ++counter;
    // }
    // --boundary;
    // ++counter;
  }
  return counter;
}

int main() {
  VecOfVecOfStr v = read_file("example.in");
  int number_of_examples = stol(v[0][0]);
  // cout << "number of examples: " << number_of_examples << endl;
  for (int i = 1; i < number_of_examples + 1; ++i) {
    cout << "Case #" << i << ": " << count(stoll(v[i][0])) << endl;
  }

  // cout<<count(23)<<endl;
  return 0;
}
