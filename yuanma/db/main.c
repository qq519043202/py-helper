#include <windows.h>
#include <stdio.h>
#include <mysql.h>
#include <string.h>

int main(int argc, char **argv)
{
	MYSQL mysql_conn; /* Connection handle */

    MYSQL_RES *mysql_result; /* Result handle */
    MYSQL_ROW mysql_row; /* Row data */

    MYSQL_FIELD *field;

    FILE *fp;



    int f1, f2, num_row, num_col,i;

    char a[100],b[100],q[100],re[100],sql[100]="select * from hanshu0 where name like '%";

    if((fp = fopen("txt//sou.txt","r"))==NULL)
    {
        printf("wrong");
        exit(0);
    }
    fscanf(fp,"%s",q);
 //   puts(q);

	if (mysql_init(&mysql_conn) != NULL)
    {

	//	printf("----------------Init succeeds!\n");

	}
    else
    {
		printf("Init fails!\n");
		exit(0);
	}
/*
	printf("user:");
	gets(a);
	printf("password:");
	gets(b);
    printf("which database?\n");
    gets(q);*/

    if (mysql_real_connect(
    &mysql_conn, "localhost","root",
    "root", "hanshu", MYSQL_PORT,
    NULL, 0) != NULL)
    {
 //       printf("----------------Link start!\n");
    }

    else
    {
        printf("----------------Connection fails.\n");
        exit(0);
    }


/*    printf("input your SQL:\n");

    gets(q);

    if(mysql_query(&mysql_conn, q))//成功返回0
    {
        printf("%s\n", mysql_error(&mysql_conn));
        exit(0);
    }*/

   /*  printf("输入你要搜索的函数名（模糊搜索）:\n");
    gets(q);*/

    strcat(sql,q);
    strcat(sql,"%'");

    if(mysql_query(&mysql_conn, sql))//成功返回0
    {
        printf("%s\n", mysql_error(&mysql_conn));
        exit(0);
    }

    mysql_result = mysql_store_result(&mysql_conn);
/*    if(mysql_result!=NULL)
    {
        printf("-----------获取结果集成功\n");
    }
    else
    {
        printf("----------获取结果集失败\n");
        exit(0);
    }*/

//    printf("---------引用的行数：%llu\n",mysql_affected_rows(&mysql_conn));
//返回受之前执行的update,delete,insert等查询影响的行数
    //返回被一个更新操作修改的行数，但其他许多数据库将仅仅因为记录匹配where字句而把它视为已经更新过。


    num_col = mysql_num_fields(mysql_result);
/*
    num_row = mysql_num_rows(mysql_result);

    for (f1 = 0; f1 < num_row; f1++) {
         mysql_row = mysql_fetch_row(mysql_result);

         for (f2 = 0; f2 < num_col; f2++)
              printf("[Row %d, Col %d] ==> [%s]\n",f1+1, f2+1, mysql_row[f2]);
        }*/
if(mysql_affected_rows(&mysql_conn)==0)
{
    printf("nothing to search");
        system("pause");
    return 0;

}

 while ((mysql_row = mysql_fetch_row(mysql_result)))
  {
      for(i = 0; i < num_col; i++)
      {
          if (i == 0) { while(field = mysql_fetch_field(mysql_result)) {
                printf("%s ", field->name);
             }
          printf("\n");
          }

          printf("%s ", mysql_row[i] ? mysql_row[i] : "NULL");
      }
      printf("\n");
  }

    /* Free the result to release the heap memory*/
    mysql_free_result(mysql_result);

    mysql_close(&mysql_conn);
    system("pause");
	return 0;
}
