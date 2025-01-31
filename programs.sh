#!/bin/bash
fact() {
  if (( $1 <= 1 )); then
    echo 1
    return
  fi
  echo $(( $1 * $(fact $(( $1 - 1 ))) ))
}

# Pls write these below program in Shell Script
# - take input from console and try to write modular code with implementing method

# 1> Check if a Number is Even or Odd
even_odd() {
  if [[ $(( $1 & 1 )) == 0 ]] ; then
    echo "even"
  else
    echo "odd"
  fi
}

# read -p "enter a number: " n
# even_odd n

# 2> Find the Largest of Three Numbers
largest_of_3_numbers() {
  local num1=$1
  local num2=$2
  local num3=$3

  if [[ num1 -eq num2 && num2 == num3 ]]; then
    echo "all are equal"
  elif [[ num1 -gt num2 && num1 -gt num3 ]]; then
    echo $num1 " is grater"
  elif [[ num2 -gt num1 && num2 -gt num3 ]]; then
    echo $num2 " is grater"

  elif [[ num3 -gt num1 && num3 -gt num2 ]]; then
    echo $num3 "is grater"
  fi
}

# read -p "Enter num1: " num1
# read -p "Enter num2: " num2
# read -p "Enter num3: " num3
#
# largest_of_3_numbers $num1 $num2 $num3


#3> Reverse a String
reverse_string() {
  local st=$1
  local n=${#st}
  local rev=""
  for ((i = n - 1; i > -1; -- i )) 
  do
    rev="$rev${st:i:1}"
  done
  echo $rev
}

# read -p "Enter a string: " st
# reverse_string $st


# 4> Check Prime Number
is_prime() {
  local n=$1
  if ((n < 2)); then
    echo "not prime"
    return
  fi

  if ((n == 2)); then
    echo "prime"
    return
  fi
  for ((i = 2; i * i <= n; ++ i ))
  do
    if ((n % i == 0)); then
      echo "not prime"
      return
    fi
  done
  echo "prime"
  return
}




# read -p "Enter a number: " n
# is_prime $n


# 5> Count Occurrences of a Character in a String
occurances() {

  declare -A letters
  local st=$1
  local n=${#st}
  for ((i = 0; i < n; ++ i))
  do
    ((letters[${st:i:1}]++))
  done
  for char in "${!letters[@]}"; do
    echo "$char: ${letters[$char]}"
  done
}


# 6> Count no of words in a given string
words_count() {
  local st=$@
  count=$(echo $st | wc -w)
  echo $count
}

# read -p  "Enter the sentance: " st
# words_count $st

prime_sum() {
  mini=$1
  maxi=$2
  echo "hii"
  sum=0
  for((i = mini; i <= maxi; ++ i))
  do
    res=$(is_prime $i)
    echo $i "is" $res
    if [[ $res == 'prime' ]]; then
      sum=$((sum + i))
    fi
  done

  echo "total:" $sum
}

prime_sum $1 $2
