defmodule Math do

  def sqrt(x) do
    refine x, x / 2.0, 1.0
  end

  def refine(target, _, attempt) when attempt * attempt == target do
    attempt
  end

  def refine(_, adjustment, attempt) when abs(attempt - (attempt - adjustment)) < 1.0e-20 do
    attempt
  end

  def refine(target, adjustment, attempt) when attempt*attempt > target do
    refine(target, adjustment / 2, attempt - adjustment)
  end

  def refine(target, adjustment, attempt) when attempt*attempt < target do
    refine(target, adjustment, attempt + adjustment)
  end

  def pow_2(n) do
      n * n
  end

end

defmodule Solution do

    def read do
        String.trim(IO.gets "")
    end

    def read_integer_from_stdin do
        read()
            |> String.to_integer
    end

    def read_coordinate do
        read()
            |> String.split(" ")
            |> Enum.map(fn x -> String.to_integer(x) end)
    end

    def read_coordinates(n) when n <= 1 do
        [read_coordinate()]
    end
    def read_coordinates(n) when n > 1 do
        [read_coordinate()] ++ read_coordinates(n - 1)
    end

    def calc_side_length(a, b) do
        Math.sqrt(Math.pow_2(Enum.at(a, 0) - Enum.at(b, 0)) + Math.pow_2(Enum.at(a, 1) - Enum.at(b, 1)))
    end

    def calc_sides_lengths(coordinates, i) when length(coordinates) - 1 == i  do
        [calc_side_length(Enum.at(coordinates, i), Enum.at(coordinates, 0))]
    end
    def calc_sides_lengths(coordinates, i) do
        [calc_side_length(Enum.at(coordinates, i), Enum.at(coordinates, i+1))] ++ calc_sides_lengths(coordinates, i + 1)
    end
end

Solution.read_integer_from_stdin
    |> Solution.read_coordinates
    |> Solution.calc_sides_lengths(0)
    |> Enum.reduce(fn(x, acc) -> x + acc end)
    |> IO.puts
