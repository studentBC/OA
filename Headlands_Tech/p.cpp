#include <iostream>  // I/O 
#include <fstream>   // file I/O
#include <iomanip>   // format manipulation
#include <string>
#include<vector>
#include <map>
#include <unordered_set>
#include<sstream>
using namespace std;

map<int, pair<double, int> >job;
unordered_set<int>beenTo;

void go (int start, double& sum, double& count, int& last) {
    if (beenTo.count(start) || !start) return;
    last = start;
    sum+=job[start].first;
    count++;
    beenTo.insert(start);
    go (job[start].second, sum, count, last);
}
string getTime(int value) {
  std::string result;
  // compute h, m, s
  std::string h = std::to_string(value / 3600);
  std::string m = std::to_string((value % 3600) / 60);
  std::string s = std::to_string(value % 60);
  // add leading zero if needed
  std::string hh = std::string(2 - h.length(), '0') + h;
  std::string mm = std::string(2 - m.length(), '0') + m;
  std::string ss = std::string(2 - s.length(), '0') + s;
  // return mm:ss if hh is 00
  //if (hh.compare("00") != 0) {
    result = hh + ':' + mm + ":" + ss;
//   }
//   else {
//     result =  mm + ":" + ss;
//   }
  return result;
}
int main(int argc, char* argv[])
{
    ifstream exprFile(argv[1]); // argv[0] is the exe, not the file ;)
    string singleExpr;
    int line = 0, parent, last;
    double second, sum, count,s = 0;
    while (getline(exprFile, singleExpr)) // Gets a full line from the file
    {
        stringstream ss(singleExpr);
        vector<string> v;
        while (ss.good()) {
            string substr;
            getline(ss, substr, ',');
            //cout << substr <<", ";
            v.push_back(substr);
        }
        if (v.size() == 3 && isdigit(v[0][0])) {
            second = stod(v[1]);
            parent = stoi(v[0]);
            s+=second;
            if (job.count(parent) || second > 60 || second < 0) {
                cout<<"Malformed Input" << endl;
                return 0;
            }
            job[parent] = make_pair(second, stoi(v[2]));
        } else if (line) {
            cout<<"Malformed Input" << endl;
            return 0;
        }
        line++;
    }
    if (s > 86400) {
        cout<<"Malformed Input" << endl;
        return 0;
    }
    cout <<endl << "-"<< endl;
    for (auto& it: job) {
        count = sum = 0;
        if (!beenTo.count(it.first)) {
            go (it.first, sum, count, last);
        
            cout << "start_job: "<<it.first << endl;
            cout << "last_job: "<<last << endl;
            cout << "number_of_jobs: "<<count<< endl;
            cout << "job_chain_runtime: "<<getTime(sum)<< endl;
            cout << "average_job_time: "<< getTime(sum/count) << endl;
            cout <<"-"<< endl;
        }
    }
    return 0;
}