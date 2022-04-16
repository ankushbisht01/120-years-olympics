#include <iostream>
using namespace std;


class matrix{
    private:
        int rows, columns;
        int **matrx;
    public:
        matrix(int value1 , int value2){
                rows = value1;
                columns = value2;
                matrx = new int*[rows];
                for (int i =0;i<rows;i++){
                    matrx[i] = new int[columns];
                }

        }

        void insert_elem(){
            for (int i = 0 ;i<rows;i++){
                for (int j=0;j<columns;j++){
                    cout<<"arr["<<i<<"]["<<j<<"] "<<endl;
                    cin>>matrx[i][j];
                    
                }
            }
        }
        int** getmatrix(){
            return matrx;
        }
        void display_matrix(){
            cout<<"["<<endl;
            for (int i =0 ;i<rows;i++){
                cout<<"[ ";
                for (int j =0 ;j<columns;j++){
                        cout<<matrx[i][j]<<" ";
                        
                }
                cout<<" ]\n";
            }
            cout<<" ] \n";
        }
        void addition(matrix b){
            int sum ;
            int **mat2 = b.getmatrix();
            cout<<"addition of these two matrix are : \n["<<endl;
            for (int i =0 ;i<rows;i++){
                cout<<"[ ";
                for (int j =0 ;j<columns;j++){
                        sum = matrx[i][j] + mat2[i][j];
                        cout<<sum<<" ";
                }
                cout<<" ]\n";
            }
            cout<<" ] \n";
            
        }
        void subtraction(matrix b){
            int subtract ;
            int **mat2 = b.getmatrix();
            cout<<"subtraction of these two matrix are : \n["<<endl;
            for (int i =0 ;i<rows;i++){
                cout<<"[ ";
                for (int j =0 ;j<columns;j++){
                        subtract = matrx[i][j]-mat2[i][j];
                        cout<<subtract
						<<" ";
                }
                cout<<" ]\n";
            }
            cout<<" ] \n";

        }
        void transpose(){
            //cout<<"transpose of matrix is  matrix are : \n["<<endl;
            cout<<"["<<endl;
            for (int i =0 ;i<columns;i++){
                cout<<"[ ";
                for (int j =0 ;j<rows;j++){
                        cout<<matrx[j][i]<<" ";
                        
                }
                cout<<" ]\n";
            }
            cout<<" ] \n";
        }
};

int main(){
    int rows, columns;
    cout <<"enter the number of rows: "<<endl;
    cin >> rows;
    cout<<"enter the number of columns : "<<endl;
    cin>>columns;
    class matrix m1(rows,columns);
    class matrix m2(rows,columns);
    cout<<"insert the elements of the first matrix\n";
    m1.insert_elem();
    cout<<"\ninsert the elements of the second matrix\n";
    m2.insert_elem();
    cout<<"first matrix is \n";
    m1.display_matrix();
    cout<<"second matrix is \n";
    m2.display_matrix();
    m1.addition(m2);
    m1.subtraction(m2);
    cout<<"transpose of first matrix: \n";
    m1.transpose();
    cout<<"transpose of second matrix: \n";
    m2.transpose();
    
}