from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

matching_dlp_rule = lazy_import('msgraph.generated.models.matching_dlp_rule')

class DlpPoliciesJobResult(AdditionalDataHolder, Parsable):
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
    
    @property
    def audit_correlation_id(self,) -> Optional[str]:
        """
        Gets the auditCorrelationId property value. The auditCorrelationId property
        Returns: Optional[str]
        """
        return self._audit_correlation_id
    
    @audit_correlation_id.setter
    def audit_correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the auditCorrelationId property value. The auditCorrelationId property
        Args:
            value: Value to set for the auditCorrelationId property.
        """
        self._audit_correlation_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new dlpPoliciesJobResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The auditCorrelationId property
        self._audit_correlation_id: Optional[str] = None
        # The evaluationDateTime property
        self._evaluation_date_time: Optional[datetime] = None
        # The matchingRules property
        self._matching_rules: Optional[List[matching_dlp_rule.MatchingDlpRule]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpPoliciesJobResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DlpPoliciesJobResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DlpPoliciesJobResult()
    
    @property
    def evaluation_date_time(self,) -> Optional[datetime]:
        """
        Gets the evaluationDateTime property value. The evaluationDateTime property
        Returns: Optional[datetime]
        """
        return self._evaluation_date_time
    
    @evaluation_date_time.setter
    def evaluation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the evaluationDateTime property value. The evaluationDateTime property
        Args:
            value: Value to set for the evaluationDateTime property.
        """
        self._evaluation_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audit_correlation_id": lambda n : setattr(self, 'audit_correlation_id', n.get_str_value()),
            "evaluation_date_time": lambda n : setattr(self, 'evaluation_date_time', n.get_datetime_value()),
            "matching_rules": lambda n : setattr(self, 'matching_rules', n.get_collection_of_object_values(matching_dlp_rule.MatchingDlpRule)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def matching_rules(self,) -> Optional[List[matching_dlp_rule.MatchingDlpRule]]:
        """
        Gets the matchingRules property value. The matchingRules property
        Returns: Optional[List[matching_dlp_rule.MatchingDlpRule]]
        """
        return self._matching_rules
    
    @matching_rules.setter
    def matching_rules(self,value: Optional[List[matching_dlp_rule.MatchingDlpRule]] = None) -> None:
        """
        Sets the matchingRules property value. The matchingRules property
        Args:
            value: Value to set for the matchingRules property.
        """
        self._matching_rules = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("auditCorrelationId", self.audit_correlation_id)
        writer.write_datetime_value("evaluationDateTime", self.evaluation_date_time)
        writer.write_collection_of_object_values("matchingRules", self.matching_rules)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

