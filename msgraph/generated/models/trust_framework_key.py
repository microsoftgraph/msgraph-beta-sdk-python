from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TrustFrameworkKey(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new trustFrameworkKey and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # RSA Key - private exponent. Field cannot be read back.
        self._d: Optional[str] = None
        # RSA Key - first exponent. Field cannot be read back.
        self._dp: Optional[str] = None
        # RSA Key - second exponent. Field cannot be read back.
        self._dq: Optional[str] = None
        # RSA Key - public exponent
        self._e: Optional[str] = None
        # This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        self._exp: Optional[int] = None
        # Symmetric Key for oct key type. Field cannot be read back.
        self._k: Optional[str] = None
        # The unique identifier for the key.
        self._kid: Optional[str] = None
        # The kty (key type) parameter identifies the cryptographic algorithm family used with the key, The valid values are rsa, oct.
        self._kty: Optional[str] = None
        # RSA Key - modulus
        self._n: Optional[str] = None
        # This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        self._nbf: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # RSA Key - first prime. Field cannot be read back.
        self._p: Optional[str] = None
        # RSA Key - second prime. Field cannot be read back.
        self._q: Optional[str] = None
        # RSA Key - Coefficient. Field cannot be read back.
        self._qi: Optional[str] = None
        # The use (public key use) parameter identifies the intended use of the public key.  The use parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Possible values are: sig (signature), enc (encryption)
        self._use: Optional[str] = None
        # The x5c (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates RFC 5280.
        self._x5c: Optional[List[str]] = None
        # The x5t (X.509 certificate SHA-1 thumbprint) parameter is a base64url-encoded SHA-1 thumbprint (a.k.a. digest) of the DER encoding of an X.509 certificate RFC 5280.
        self._x5t: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrustFrameworkKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TrustFrameworkKey
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TrustFrameworkKey()
    
    @property
    def d(self,) -> Optional[str]:
        """
        Gets the d property value. RSA Key - private exponent. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._d
    
    @d.setter
    def d(self,value: Optional[str] = None) -> None:
        """
        Sets the d property value. RSA Key - private exponent. Field cannot be read back.
        Args:
            value: Value to set for the d property.
        """
        self._d = value
    
    @property
    def dp(self,) -> Optional[str]:
        """
        Gets the dp property value. RSA Key - first exponent. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._dp
    
    @dp.setter
    def dp(self,value: Optional[str] = None) -> None:
        """
        Sets the dp property value. RSA Key - first exponent. Field cannot be read back.
        Args:
            value: Value to set for the dp property.
        """
        self._dp = value
    
    @property
    def dq(self,) -> Optional[str]:
        """
        Gets the dq property value. RSA Key - second exponent. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._dq
    
    @dq.setter
    def dq(self,value: Optional[str] = None) -> None:
        """
        Sets the dq property value. RSA Key - second exponent. Field cannot be read back.
        Args:
            value: Value to set for the dq property.
        """
        self._dq = value
    
    @property
    def e(self,) -> Optional[str]:
        """
        Gets the e property value. RSA Key - public exponent
        Returns: Optional[str]
        """
        return self._e
    
    @e.setter
    def e(self,value: Optional[str] = None) -> None:
        """
        Sets the e property value. RSA Key - public exponent
        Args:
            value: Value to set for the e property.
        """
        self._e = value
    
    @property
    def exp(self,) -> Optional[int]:
        """
        Gets the exp property value. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Returns: Optional[int]
        """
        return self._exp
    
    @exp.setter
    def exp(self,value: Optional[int] = None) -> None:
        """
        Sets the exp property value. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Args:
            value: Value to set for the exp property.
        """
        self._exp = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "d": lambda n : setattr(self, 'd', n.get_str_value()),
            "dp": lambda n : setattr(self, 'dp', n.get_str_value()),
            "dq": lambda n : setattr(self, 'dq', n.get_str_value()),
            "e": lambda n : setattr(self, 'e', n.get_str_value()),
            "exp": lambda n : setattr(self, 'exp', n.get_int_value()),
            "k": lambda n : setattr(self, 'k', n.get_str_value()),
            "kid": lambda n : setattr(self, 'kid', n.get_str_value()),
            "kty": lambda n : setattr(self, 'kty', n.get_str_value()),
            "n": lambda n : setattr(self, 'n', n.get_str_value()),
            "nbf": lambda n : setattr(self, 'nbf', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "p": lambda n : setattr(self, 'p', n.get_str_value()),
            "q": lambda n : setattr(self, 'q', n.get_str_value()),
            "qi": lambda n : setattr(self, 'qi', n.get_str_value()),
            "use": lambda n : setattr(self, 'use', n.get_str_value()),
            "x5c": lambda n : setattr(self, 'x5c', n.get_collection_of_primitive_values(str)),
            "x5t": lambda n : setattr(self, 'x5t', n.get_str_value()),
        }
        return fields
    
    @property
    def k(self,) -> Optional[str]:
        """
        Gets the k property value. Symmetric Key for oct key type. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._k
    
    @k.setter
    def k(self,value: Optional[str] = None) -> None:
        """
        Sets the k property value. Symmetric Key for oct key type. Field cannot be read back.
        Args:
            value: Value to set for the k property.
        """
        self._k = value
    
    @property
    def kid(self,) -> Optional[str]:
        """
        Gets the kid property value. The unique identifier for the key.
        Returns: Optional[str]
        """
        return self._kid
    
    @kid.setter
    def kid(self,value: Optional[str] = None) -> None:
        """
        Sets the kid property value. The unique identifier for the key.
        Args:
            value: Value to set for the kid property.
        """
        self._kid = value
    
    @property
    def kty(self,) -> Optional[str]:
        """
        Gets the kty property value. The kty (key type) parameter identifies the cryptographic algorithm family used with the key, The valid values are rsa, oct.
        Returns: Optional[str]
        """
        return self._kty
    
    @kty.setter
    def kty(self,value: Optional[str] = None) -> None:
        """
        Sets the kty property value. The kty (key type) parameter identifies the cryptographic algorithm family used with the key, The valid values are rsa, oct.
        Args:
            value: Value to set for the kty property.
        """
        self._kty = value
    
    @property
    def n(self,) -> Optional[str]:
        """
        Gets the n property value. RSA Key - modulus
        Returns: Optional[str]
        """
        return self._n
    
    @n.setter
    def n(self,value: Optional[str] = None) -> None:
        """
        Sets the n property value. RSA Key - modulus
        Args:
            value: Value to set for the n property.
        """
        self._n = value
    
    @property
    def nbf(self,) -> Optional[int]:
        """
        Gets the nbf property value. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Returns: Optional[int]
        """
        return self._nbf
    
    @nbf.setter
    def nbf(self,value: Optional[int] = None) -> None:
        """
        Sets the nbf property value. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Args:
            value: Value to set for the nbf property.
        """
        self._nbf = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def p(self,) -> Optional[str]:
        """
        Gets the p property value. RSA Key - first prime. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._p
    
    @p.setter
    def p(self,value: Optional[str] = None) -> None:
        """
        Sets the p property value. RSA Key - first prime. Field cannot be read back.
        Args:
            value: Value to set for the p property.
        """
        self._p = value
    
    @property
    def q(self,) -> Optional[str]:
        """
        Gets the q property value. RSA Key - second prime. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._q
    
    @q.setter
    def q(self,value: Optional[str] = None) -> None:
        """
        Sets the q property value. RSA Key - second prime. Field cannot be read back.
        Args:
            value: Value to set for the q property.
        """
        self._q = value
    
    @property
    def qi(self,) -> Optional[str]:
        """
        Gets the qi property value. RSA Key - Coefficient. Field cannot be read back.
        Returns: Optional[str]
        """
        return self._qi
    
    @qi.setter
    def qi(self,value: Optional[str] = None) -> None:
        """
        Sets the qi property value. RSA Key - Coefficient. Field cannot be read back.
        Args:
            value: Value to set for the qi property.
        """
        self._qi = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("d", self.d)
        writer.write_str_value("dp", self.dp)
        writer.write_str_value("dq", self.dq)
        writer.write_str_value("e", self.e)
        writer.write_int_value("exp", self.exp)
        writer.write_str_value("k", self.k)
        writer.write_str_value("kid", self.kid)
        writer.write_str_value("kty", self.kty)
        writer.write_str_value("n", self.n)
        writer.write_int_value("nbf", self.nbf)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("p", self.p)
        writer.write_str_value("q", self.q)
        writer.write_str_value("qi", self.qi)
        writer.write_str_value("use", self.use)
        writer.write_collection_of_primitive_values("x5c", self.x5c)
        writer.write_str_value("x5t", self.x5t)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def use(self,) -> Optional[str]:
        """
        Gets the use property value. The use (public key use) parameter identifies the intended use of the public key.  The use parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Possible values are: sig (signature), enc (encryption)
        Returns: Optional[str]
        """
        return self._use
    
    @use.setter
    def use(self,value: Optional[str] = None) -> None:
        """
        Sets the use property value. The use (public key use) parameter identifies the intended use of the public key.  The use parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Possible values are: sig (signature), enc (encryption)
        Args:
            value: Value to set for the use property.
        """
        self._use = value
    
    @property
    def x5c(self,) -> Optional[List[str]]:
        """
        Gets the x5c property value. The x5c (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates RFC 5280.
        Returns: Optional[List[str]]
        """
        return self._x5c
    
    @x5c.setter
    def x5c(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the x5c property value. The x5c (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates RFC 5280.
        Args:
            value: Value to set for the x5c property.
        """
        self._x5c = value
    
    @property
    def x5t(self,) -> Optional[str]:
        """
        Gets the x5t property value. The x5t (X.509 certificate SHA-1 thumbprint) parameter is a base64url-encoded SHA-1 thumbprint (a.k.a. digest) of the DER encoding of an X.509 certificate RFC 5280.
        Returns: Optional[str]
        """
        return self._x5t
    
    @x5t.setter
    def x5t(self,value: Optional[str] = None) -> None:
        """
        Sets the x5t property value. The x5t (X.509 certificate SHA-1 thumbprint) parameter is a base64url-encoded SHA-1 thumbprint (a.k.a. digest) of the DER encoding of an X.509 certificate RFC 5280.
        Args:
            value: Value to set for the x5t property.
        """
        self._x5t = value
    

