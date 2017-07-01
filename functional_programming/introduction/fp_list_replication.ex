defmodule Solution do
    def read do
        String.trim(IO.gets "")
    end

    def keep_reading(n) do
        print_element(n, read())
    end

    def print_element(n, e) when e != nil do
        print_element_n_times(n, e)
        keep_reading(n)
    end

    def print_element_n_times(n, e) when n <= 1 do
        IO.puts e
    end

    def print_element_n_times(n, e) do
        IO.puts e
        print_element_n_times(n - 1, e)
    end
end

Solution.read
    |> String.to_integer
    |> Solution.keep_reading
