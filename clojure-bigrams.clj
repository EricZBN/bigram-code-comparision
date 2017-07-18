(ns clojure-bigrams.core
  (:gen-class))


(defn remove-punctuation
    [string]
    (clojure.string/replace string #"[^0-9a-zA-Z\s]" ""))

(defn get-clean-text
    [file-in]
    (clojure.string/split (.toLowerCase (remove-punctuation (slurp file-in))) #"\s+"))

(defn create-bigram-vector
    [string-vec-in]
    (vec (map vector string-vec-in (rest string-vec-in))))

(defn create-bigram-output-set
    [vec-vec-in]
    (frequencies vec-vec-in))

(defn bigram-histogram
   [bigram-output-set-in]
   (doseq [i  bigram-output-set-in]
     (println (format "%s %s - %s"
       (get(get i 0) 0)
       (get(get i 0) 1)
       (apply str (repeat (get i 1) \*))))
    )
  )

(defn -main
  [& args]
    (println)
    (bigram-histogram(create-bigram-output-set(create-bigram-vector
    (get-clean-text "bg_input_text.txt"))))
    (println)
  )
