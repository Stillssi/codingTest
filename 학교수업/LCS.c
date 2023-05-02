#include <stdio.h>
#include <math.h>

#define N 100
#define W 5
typedef struct {
    int x, y;
} Point;

void read_contour_points(Point h[]){
    //읽을 파일
}

double cal_lcs(Point contour[], int i ){
    int left = i - (w-1)/2;
    int right = i + (w-1)/2;
    
    double u_i = h[i].x * (h[left].y - h[right].y) + 
                 h[i].y * (h[right].x - h[left].x) +
                 h[right].y * h[left].x - h[left].y * h[right].x;
    double v_i = sqrt(pow(h[left].y - h[right].y) + pow(h[left].x - h[right]/x));
   
    return fabs(u_i/v_i)
}

int main(){
    Point h[N];
    read_contour_points(h);
    
    for (int i=0; i<N; i++){
        double lcs = cal_lcs(h, i);
        printf("LCS h(%d) = %.2f\n",i,lcs);
    }
    return 0
}


