#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <fstream>
#include <sstream>
using std::string;
using std::vector;
using std::ifstream;
using std::stringstream;
using std::cout;
using std::endl;
using std::size_t;
using std::to_string;
using std::rotate;
using std::stoi;

typedef vector<vector<string> > VecOfVecOfStrings;

vector<string> V = {"ZERO", "ONE", "TWO",   "THREE", "FOUR",
                    "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
                   };

struct example {
    string number;
    string tel;
    int vec_shift;
};

VecOfVecOfStrings read_file(string file_name, bool print_console = false) {
    string line;
    VecOfVecOfStrings v;
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
        for (const vector<string>& vec : v) {
            for (string x : vec) cout << x << ' ';
            cout << endl;
        }
    }
    return v;
}

example digit_in_string(string digit, example exmpl) {
    if (exmpl.number.empty()) return exmpl;
    example new_exmpl = exmpl;
    size_t found;
    for (char& c : digit) {
        found = new_exmpl.number.find(c);
        if (found == string::npos) return exmpl;
        new_exmpl.number.erase(new_exmpl.number.begin() + found);
    }
    vector<string>::iterator it;
    it = find(V.begin(), V.end(), digit);
    size_t i = it - V.begin();
    new_exmpl.tel += to_string(i);
    return digit_in_string(digit, new_exmpl);
}

example test_all(example exmpl) {
    example new_exmpl = exmpl;
    vector<string> new_V = V;
    cout << new_exmpl.vec_shift << endl;
    rotate(new_V.begin(), new_V.begin() + new_exmpl.vec_shift, new_V.end());
    for (int i = 0; i < new_V.size(); ++i) {
        new_exmpl = digit_in_string(new_V[i], new_exmpl);
    }
    if (new_exmpl.number != "") {
        exmpl.vec_shift += 1;
        test_all(exmpl);
    } else {
        cout << new_exmpl.number << endl;
        cout << "tel:" << new_exmpl.tel << endl;
        return new_exmpl;
    }
}

int main(int argc, char const* argv[]) {
    VecOfVecOfStrings f = read_file("A2.in");
    // for (int i = 0; i < stoi(f[0][0]); ++i) {
    example test;
    int i = 98;
    test.number = f[i + 1][0];
    test.vec_shift = 0;
    example k = test_all(test);
    cout << k.tel << endl;
    // }
    return 0;
}
