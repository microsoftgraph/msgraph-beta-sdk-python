from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_connection = lazy_import('msgraph.generated.models.teamwork_connection')

class TeamworkLoginStatus(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamworkLoginStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Information about the Exchange connection.
        self._exchange_connection: Optional[teamwork_connection.TeamworkConnection] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Information about the Skype for Business connection.
        self._skype_connection: Optional[teamwork_connection.TeamworkConnection] = None
        # Information about the Teams connection.
        self._teams_connection: Optional[teamwork_connection.TeamworkConnection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkLoginStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkLoginStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkLoginStatus()
    
    @property
    def exchange_connection(self,) -> Optional[teamwork_connection.TeamworkConnection]:
        """
        Gets the exchangeConnection property value. Information about the Exchange connection.
        Returns: Optional[teamwork_connection.TeamworkConnection]
        """
        return self._exchange_connection
    
    @exchange_connection.setter
    def exchange_connection(self,value: Optional[teamwork_connection.TeamworkConnection] = None) -> None:
        """
        Sets the exchangeConnection property value. Information about the Exchange connection.
        Args:
            value: Value to set for the exchangeConnection property.
        """
        self._exchange_connection = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exchange_connection": lambda n : setattr(self, 'exchange_connection', n.get_object_value(teamwork_connection.TeamworkConnection)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skype_connection": lambda n : setattr(self, 'skype_connection', n.get_object_value(teamwork_connection.TeamworkConnection)),
            "teams_connection": lambda n : setattr(self, 'teams_connection', n.get_object_value(teamwork_connection.TeamworkConnection)),
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
        writer.write_object_value("exchangeConnection", self.exchange_connection)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("skypeConnection", self.skype_connection)
        writer.write_object_value("teamsConnection", self.teams_connection)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def skype_connection(self,) -> Optional[teamwork_connection.TeamworkConnection]:
        """
        Gets the skypeConnection property value. Information about the Skype for Business connection.
        Returns: Optional[teamwork_connection.TeamworkConnection]
        """
        return self._skype_connection
    
    @skype_connection.setter
    def skype_connection(self,value: Optional[teamwork_connection.TeamworkConnection] = None) -> None:
        """
        Sets the skypeConnection property value. Information about the Skype for Business connection.
        Args:
            value: Value to set for the skypeConnection property.
        """
        self._skype_connection = value
    
    @property
    def teams_connection(self,) -> Optional[teamwork_connection.TeamworkConnection]:
        """
        Gets the teamsConnection property value. Information about the Teams connection.
        Returns: Optional[teamwork_connection.TeamworkConnection]
        """
        return self._teams_connection
    
    @teams_connection.setter
    def teams_connection(self,value: Optional[teamwork_connection.TeamworkConnection] = None) -> None:
        """
        Sets the teamsConnection property value. Information about the Teams connection.
        Args:
            value: Value to set for the teamsConnection property.
        """
        self._teams_connection = value
    

