IO.stream(:stdio, :line)
    |> Enum.reduce(0, fn x, y -> y + 1 end)
    |> IO.puts
