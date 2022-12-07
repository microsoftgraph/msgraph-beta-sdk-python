from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_on_premises_calendar_sync_configuration = lazy_import('msgraph.generated.models.teamwork_on_premises_calendar_sync_configuration')
teamwork_supported_client = lazy_import('msgraph.generated.models.teamwork_supported_client')

class TeamworkAccountConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamworkAccountConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The account used to sync the calendar.
        self._on_premises_calendar_sync_configuration: Optional[teamwork_on_premises_calendar_sync_configuration.TeamworkOnPremisesCalendarSyncConfiguration] = None
        # The supported client for Teams Rooms devices. The possible values are: unknown, skypeDefaultAndTeams, teamsDefaultAndSkype, skypeOnly, teamsOnly, unknownFutureValue.
        self._supported_client: Optional[teamwork_supported_client.TeamworkSupportedClient] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkAccountConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkAccountConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkAccountConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_premises_calendar_sync_configuration": lambda n : setattr(self, 'on_premises_calendar_sync_configuration', n.get_object_value(teamwork_on_premises_calendar_sync_configuration.TeamworkOnPremisesCalendarSyncConfiguration)),
            "supported_client": lambda n : setattr(self, 'supported_client', n.get_enum_value(teamwork_supported_client.TeamworkSupportedClient)),
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
    
    @property
    def on_premises_calendar_sync_configuration(self,) -> Optional[teamwork_on_premises_calendar_sync_configuration.TeamworkOnPremisesCalendarSyncConfiguration]:
        """
        Gets the onPremisesCalendarSyncConfiguration property value. The account used to sync the calendar.
        Returns: Optional[teamwork_on_premises_calendar_sync_configuration.TeamworkOnPremisesCalendarSyncConfiguration]
        """
        return self._on_premises_calendar_sync_configuration
    
    @on_premises_calendar_sync_configuration.setter
    def on_premises_calendar_sync_configuration(self,value: Optional[teamwork_on_premises_calendar_sync_configuration.TeamworkOnPremisesCalendarSyncConfiguration] = None) -> None:
        """
        Sets the onPremisesCalendarSyncConfiguration property value. The account used to sync the calendar.
        Args:
            value: Value to set for the onPremisesCalendarSyncConfiguration property.
        """
        self._on_premises_calendar_sync_configuration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("onPremisesCalendarSyncConfiguration", self.on_premises_calendar_sync_configuration)
        writer.write_enum_value("supportedClient", self.supported_client)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def supported_client(self,) -> Optional[teamwork_supported_client.TeamworkSupportedClient]:
        """
        Gets the supportedClient property value. The supported client for Teams Rooms devices. The possible values are: unknown, skypeDefaultAndTeams, teamsDefaultAndSkype, skypeOnly, teamsOnly, unknownFutureValue.
        Returns: Optional[teamwork_supported_client.TeamworkSupportedClient]
        """
        return self._supported_client
    
    @supported_client.setter
    def supported_client(self,value: Optional[teamwork_supported_client.TeamworkSupportedClient] = None) -> None:
        """
        Sets the supportedClient property value. The supported client for Teams Rooms devices. The possible values are: unknown, skypeDefaultAndTeams, teamsDefaultAndSkype, skypeOnly, teamsOnly, unknownFutureValue.
        Args:
            value: Value to set for the supportedClient property.
        """
        self._supported_client = value
    

