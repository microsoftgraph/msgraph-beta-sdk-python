from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_account_configuration = lazy_import('msgraph.generated.models.teamwork_account_configuration')
teamwork_features_configuration = lazy_import('msgraph.generated.models.teamwork_features_configuration')

class TeamworkTeamsClientConfiguration(AdditionalDataHolder, Parsable):
    @property
    def account_configuration(self,) -> Optional[teamwork_account_configuration.TeamworkAccountConfiguration]:
        """
        Gets the accountConfiguration property value. The configuration of the Microsoft Teams client user account for a device.
        Returns: Optional[teamwork_account_configuration.TeamworkAccountConfiguration]
        """
        return self._account_configuration
    
    @account_configuration.setter
    def account_configuration(self,value: Optional[teamwork_account_configuration.TeamworkAccountConfiguration] = None) -> None:
        """
        Sets the accountConfiguration property value. The configuration of the Microsoft Teams client user account for a device.
        Args:
            value: Value to set for the accountConfiguration property.
        """
        self._account_configuration = value
    
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
        Instantiates a new teamworkTeamsClientConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The configuration of the Microsoft Teams client user account for a device.
        self._account_configuration: Optional[teamwork_account_configuration.TeamworkAccountConfiguration] = None
        # The configuration of Microsoft Teams client features for a device.
        self._features_configuration: Optional[teamwork_features_configuration.TeamworkFeaturesConfiguration] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkTeamsClientConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkTeamsClientConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkTeamsClientConfiguration()
    
    @property
    def features_configuration(self,) -> Optional[teamwork_features_configuration.TeamworkFeaturesConfiguration]:
        """
        Gets the featuresConfiguration property value. The configuration of Microsoft Teams client features for a device.
        Returns: Optional[teamwork_features_configuration.TeamworkFeaturesConfiguration]
        """
        return self._features_configuration
    
    @features_configuration.setter
    def features_configuration(self,value: Optional[teamwork_features_configuration.TeamworkFeaturesConfiguration] = None) -> None:
        """
        Sets the featuresConfiguration property value. The configuration of Microsoft Teams client features for a device.
        Args:
            value: Value to set for the featuresConfiguration property.
        """
        self._features_configuration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_configuration": lambda n : setattr(self, 'account_configuration', n.get_object_value(teamwork_account_configuration.TeamworkAccountConfiguration)),
            "features_configuration": lambda n : setattr(self, 'features_configuration', n.get_object_value(teamwork_features_configuration.TeamworkFeaturesConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("accountConfiguration", self.account_configuration)
        writer.write_object_value("featuresConfiguration", self.features_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

