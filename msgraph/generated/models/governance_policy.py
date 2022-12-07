from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

governance_criteria = lazy_import('msgraph.generated.models.governance_criteria')
governance_notification_policy = lazy_import('msgraph.generated.models.governance_notification_policy')

class GovernancePolicy(AdditionalDataHolder, Parsable):
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
        Instantiates a new governancePolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The decisionMakerCriteria property
        self._decision_maker_criteria: Optional[List[governance_criteria.GovernanceCriteria]] = None
        # The notificationPolicy property
        self._notification_policy: Optional[governance_notification_policy.GovernanceNotificationPolicy] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernancePolicy()
    
    @property
    def decision_maker_criteria(self,) -> Optional[List[governance_criteria.GovernanceCriteria]]:
        """
        Gets the decisionMakerCriteria property value. The decisionMakerCriteria property
        Returns: Optional[List[governance_criteria.GovernanceCriteria]]
        """
        return self._decision_maker_criteria
    
    @decision_maker_criteria.setter
    def decision_maker_criteria(self,value: Optional[List[governance_criteria.GovernanceCriteria]] = None) -> None:
        """
        Sets the decisionMakerCriteria property value. The decisionMakerCriteria property
        Args:
            value: Value to set for the decisionMakerCriteria property.
        """
        self._decision_maker_criteria = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "decision_maker_criteria": lambda n : setattr(self, 'decision_maker_criteria', n.get_collection_of_object_values(governance_criteria.GovernanceCriteria)),
            "notification_policy": lambda n : setattr(self, 'notification_policy', n.get_object_value(governance_notification_policy.GovernanceNotificationPolicy)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def notification_policy(self,) -> Optional[governance_notification_policy.GovernanceNotificationPolicy]:
        """
        Gets the notificationPolicy property value. The notificationPolicy property
        Returns: Optional[governance_notification_policy.GovernanceNotificationPolicy]
        """
        return self._notification_policy
    
    @notification_policy.setter
    def notification_policy(self,value: Optional[governance_notification_policy.GovernanceNotificationPolicy] = None) -> None:
        """
        Sets the notificationPolicy property value. The notificationPolicy property
        Args:
            value: Value to set for the notificationPolicy property.
        """
        self._notification_policy = value
    
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
        writer.write_collection_of_object_values("decisionMakerCriteria", self.decision_maker_criteria)
        writer.write_object_value("notificationPolicy", self.notification_policy)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

