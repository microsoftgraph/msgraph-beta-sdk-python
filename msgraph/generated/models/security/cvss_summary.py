from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import vulnerability_severity

class CvssSummary(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new cvssSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The CVSS score about this vulnerability.
        self._score: Optional[float] = None
        # The CVSS severity rating for this vulnerability. The possible values are: none, low, medium, high, critical, unknownFutureValue.
        self._severity: Optional[vulnerability_severity.VulnerabilitySeverity] = None
        # The CVSS vector string for this vulnerability.
        self._vector_string: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CvssSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CvssSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CvssSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import vulnerability_severity

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "score": lambda n : setattr(self, 'score', n.get_float_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(vulnerability_severity.VulnerabilitySeverity)),
            "vectorString": lambda n : setattr(self, 'vector_string', n.get_str_value()),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def score(self,) -> Optional[float]:
        """
        Gets the score property value. The CVSS score about this vulnerability.
        Returns: Optional[float]
        """
        return self._score
    
    @score.setter
    def score(self,value: Optional[float] = None) -> None:
        """
        Sets the score property value. The CVSS score about this vulnerability.
        Args:
            value: Value to set for the score property.
        """
        self._score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("score", self.score)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("vectorString", self.vector_string)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def severity(self,) -> Optional[vulnerability_severity.VulnerabilitySeverity]:
        """
        Gets the severity property value. The CVSS severity rating for this vulnerability. The possible values are: none, low, medium, high, critical, unknownFutureValue.
        Returns: Optional[vulnerability_severity.VulnerabilitySeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[vulnerability_severity.VulnerabilitySeverity] = None) -> None:
        """
        Sets the severity property value. The CVSS severity rating for this vulnerability. The possible values are: none, low, medium, high, critical, unknownFutureValue.
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def vector_string(self,) -> Optional[str]:
        """
        Gets the vectorString property value. The CVSS vector string for this vulnerability.
        Returns: Optional[str]
        """
        return self._vector_string
    
    @vector_string.setter
    def vector_string(self,value: Optional[str] = None) -> None:
        """
        Sets the vectorString property value. The CVSS vector string for this vulnerability.
        Args:
            value: Value to set for the vector_string property.
        """
        self._vector_string = value
    

