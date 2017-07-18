import System.IO
import Data.Char
import Data.List



cleanContents :: String -> String
cleanContents strIn =
  map toLower (filter (\x -> (isLetter x) || (isDigit x) || (isSpace x)) strIn)

bigramTupleList :: String -> [(String, String)]
bigramTupleList strIn = zip (words strIn) (tail (words strIn))

frequency :: Ord t => [t] -> [(Int, t)]
frequency listIn = map (\l -> (length l, head l)) (group (sort listIn))




main = do
    contents <- getContents
    mapM (putStrLn . show) (frequency (bigramTupleList (cleanContents contents)))
















